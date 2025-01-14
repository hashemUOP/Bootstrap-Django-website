function showPopup() {
        document.getElementById('popup').classList.add('popup-visible');
        document.getElementById('popup-overlay').classList.add('popup-overlay-visible');
    }

    function hidePopup() {
        document.getElementById('popup').classList.remove('popup-visible');
        document.getElementById('popup-overlay').classList.remove('popup-overlay-visible');
    }

//this code is for the laptop page