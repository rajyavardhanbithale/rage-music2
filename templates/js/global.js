const exiTime = 30; // In Second

if (window.innerWidth <= 600) {
    const musicTitle = document.querySelector('.music-title');
    if (musicTitle.textContent.length > 20) {
        musicTitle.classList.add('animated-text');
    }
}

function showDiv() {
    var bar = document.getElementById('bar');
    var navigation = document.getElementById('navigation');

    bar.classList.add('entry-animation');
    setTimeout(function () {
        bar.style.display = 'none';
        bar.classList.remove('entry-animation');
        navigation.style.display = 'block';
    }, 300);

    setTimeout(function () {
        bar.style.display = 'block';
        bar.classList.add('visible');
        navigation.style.display = 'none';
    }, (exiTime * 1000));

    setTimeout(function () {
        bar.classList.remove('visible');
    }, (exiTime * 100) + 100);
}

function vibratePhone(duration) {
    if (navigator.vibrate) {
      try {
        navigator.vibrate(duration);
      } catch (error) {
        console.log("Failed to vibrate the phone:", error);
      }
    } else {
      console.log("Vibration API is not supported");
    }
  }
  
  // Usage: vibrate the phone for 1 second
  vibratePhone(1000);
  