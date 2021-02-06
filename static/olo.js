function fadeIn(element, duration = 600) {
  element.style.display = '';
  element.style.opacity = 0;
  var last = +new Date();
  var tick = function() {
    console.log(element.style.opacity);
    element.style.opacity = +element.style.opacity + (new Date() - last) / duration;
    last = +new Date();
    if (+element.style.opacity < 1) {
      (window.requestAnimationFrame && requestAnimationFrame(tick)) || setTimeout(tick, 16);
    }
  };
  tick();
}

  
function fadeOut(element, duration = 600) {
  element.style.opacity = 1.035;
  var last = +new Date();
  var tick = function() {
    console.log(element.style.opacity);
    element.style.opacity = +element.style.opacity - (new Date() - last) / duration;
    last = +new Date();

    if (+element.style.opacity > -0.01) {
      (window.requestAnimationFrame && requestAnimationFrame(tick)) ||
        setTimeout(tick, 16);
    }
  };
  tick();
}