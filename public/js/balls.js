/**
 * 3D Depth Falling Balls Background Effect
 * Plain JavaScript + HTML5 2D Canvas. No external libraries.
 *
 * Simulates gentle spheres drifting downward at different depths:
 * - Far balls: smaller, slower, softer opacity
 * - Near balls: larger, faster, higher opacity, soft drop shadow
 * - Each ball has a radial gradient to give a 3D spherical highlight
 */

// Configuration settings - easy to tweak and experiment with!
var CONFIG = {
  desktopCount: 35,       // Ball count on desktop screens
  mobileCount: 18,        // Ball count on mobile screens (<860px)
  minSize: 4,             // Minimum diameter in px (far balls)
  maxSize: 22,            // Maximum diameter in px (near balls)
  minSpeed: 0.35,         // Vertical speed for farthest balls (px/frame)
  maxSpeed: 1.15,         // Vertical speed for nearest balls (px/frame)
  minOpacity: 0.14,       // Opacity of farthest balls
  maxOpacity: 0.44,       // Opacity of nearest balls (subtle, <= 0.50)
  swayMaxAmp: 0.75,       // Max horizontal sway amplitude (px/frame)
  colors: {
    // Site brand teal (#0e7c86)
    teal: {
      base: "#0e7c86",
      light: "rgba(220, 252, 250, 0.95)",
      dark: "#063e43"
    },
    // Light teal tint
    lightTeal: {
      base: "#14b8a6",
      light: "rgba(235, 254, 253, 0.95)",
      dark: "#0b5e56"
    },
    // Site accent orange (#c2410c)
    orange: {
      base: "#c2410c",
      light: "rgba(255, 240, 230, 0.95)",
      dark: "#7c2d12"
    }
  }
};

(function () {
  var canvas = document.getElementById("balls");
  if (!canvas) return;

  var ctx = canvas.getContext("2d");
  if (!ctx) return;

  var width = window.innerWidth;
  var height = window.innerHeight;
  var dpr = window.devicePixelRatio || 1;
  var balls = [];
  var animId = null;
  var isRunning = false;

  // Create an individual ball with 3D depth parameters
  function createBall(isInitial) {
    // depth: 0 = farthest, 1 = nearest
    var depth = Math.random();
    var diameter = CONFIG.minSize + depth * (CONFIG.maxSize - CONFIG.minSize);
    var radius = diameter / 2;

    // Distribute colors: ~65% teal, ~20% light teal, ~15% orange
    var randCol = Math.random();
    var theme;
    if (randCol < 0.65) {
      theme = CONFIG.colors.teal;
    } else if (randCol < 0.85) {
      theme = CONFIG.colors.lightTeal;
    } else {
      theme = CONFIG.colors.orange;
    }

    return {
      x: Math.random() * width,
      y: isInitial ? Math.random() * height : -radius * 2,
      radius: radius,
      depth: depth,
      speedY: CONFIG.minSpeed + depth * (CONFIG.maxSpeed - CONFIG.minSpeed),
      opacity: CONFIG.minOpacity + depth * (CONFIG.maxOpacity - CONFIG.minOpacity),
      colorTheme: theme,
      swayAngle: Math.random() * Math.PI * 2,
      swaySpeed: 0.012 + Math.random() * 0.018,
      swayAmp: (0.3 + depth * 0.5) * CONFIG.swayMaxAmp
    };
  }

  // Update position and wrap around edges
  function updateBall(b) {
    b.y += b.speedY;
    b.swayAngle += b.swaySpeed;
    b.x += Math.sin(b.swayAngle) * b.swayAmp;

    // Horizontal wrap
    if (b.x < -b.radius * 2) {
      b.x = width + b.radius;
    } else if (b.x > width + b.radius * 2) {
      b.x = -b.radius;
    }

    // Reset to top when ball leaves the bottom
    if (b.y - b.radius > height) {
      b.y = -b.radius * 2;
      b.x = Math.random() * width;
      b.swayAngle = Math.random() * Math.PI * 2;
    }
  }

  // Render ball as a shaded 3D sphere with radial gradient and soft shadow
  function drawBall(b) {
    ctx.save();
    ctx.globalAlpha = b.opacity;

    // Soft drop shadow only for near balls (depth > 0.55) to enhance 3D feel
    if (b.depth > 0.55) {
      ctx.shadowColor = "rgba(16, 48, 46, 0.16)";
      ctx.shadowBlur = b.radius * 0.8;
      ctx.shadowOffsetX = b.radius * 0.2;
      ctx.shadowOffsetY = b.radius * 0.35;
    }

    // Radial gradient offset towards top-left to create the sphere look
    var hlX = b.x - b.radius * 0.32;
    var hlY = b.y - b.radius * 0.32;
    var grad = ctx.createRadialGradient(
      hlX, hlY, b.radius * 0.08,
      b.x, b.y, b.radius
    );

    grad.addColorStop(0, b.colorTheme.light);
    grad.addColorStop(0.45, b.colorTheme.base);
    grad.addColorStop(1, b.colorTheme.dark);

    ctx.fillStyle = grad;
    ctx.beginPath();
    ctx.arc(b.x, b.y, b.radius, 0, Math.PI * 2);
    ctx.fill();

    ctx.restore();
  }

  // Animation frame loop
  function render() {
    ctx.clearRect(0, 0, width, height);
    for (var i = 0; i < balls.length; i++) {
      updateBall(balls[i]);
      drawBall(balls[i]);
    }
    animId = requestAnimationFrame(render);
  }

  // Start or resume loop
  function startAnimation() {
    if (isRunning) return;
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    isRunning = true;
    animId = requestAnimationFrame(render);
  }

  // Pause animation
  function stopAnimation() {
    isRunning = false;
    if (animId) {
      cancelAnimationFrame(animId);
      animId = null;
    }
  }

  // Adjust canvas size and handle high-density screens
  function resize() {
    width = window.innerWidth;
    height = window.innerHeight;
    dpr = window.devicePixelRatio || 1;

    canvas.width = Math.round(width * dpr);
    canvas.height = Math.round(height * dpr);
    canvas.style.width = width + "px";
    canvas.style.height = height + "px";
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

    // Adjust target ball count for screen size
    var targetCount = width < 860 ? CONFIG.mobileCount : CONFIG.desktopCount;
    while (balls.length < targetCount) {
      balls.push(createBall(true));
    }
    while (balls.length > targetCount) {
      balls.pop();
    }
  }

  // Setup listeners
  function init() {
    resize();
    window.addEventListener("resize", resize);

    // Pause when tab is inactive to preserve CPU / battery
    document.addEventListener("visibilitychange", function () {
      if (document.hidden) {
        stopAnimation();
      } else {
        startAnimation();
      }
    });

    // Respect user's motion preference
    var motionQuery = window.matchMedia("(prefers-reduced-motion: reduce)");
    if (motionQuery.addEventListener) {
      motionQuery.addEventListener("change", function (e) {
        if (e.matches) {
          stopAnimation();
          ctx.clearRect(0, 0, width, height);
        } else {
          startAnimation();
        }
      });
    }

    startAnimation();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
