
function goBack() {
    window.history.back();
}

function goForward() {
    window.history.forward();
}

// 알림 모달
var alertTimeout; // 자동 숨김 타이머 변수

function short_showCustomAlert(message) {
    var alertBox = document.getElementById("customAlert");
    alertBox.innerHTML = message;
    alertBox.style.display = "block";
    setTimeout(() => { alertBox.style.opacity = "1"; }, 10); // 부드럽게 나타남

    // 3초 후 자동으로 사라짐
    alertTimeout = setTimeout(hideCustomAlert, 2000);
}

function long_showCustomAlert(message) {
    var alertBox = document.getElementById("customAlert");
    alertBox.innerHTML = message;
    alertBox.style.display = "block";
    setTimeout(() => { alertBox.style.opacity = "1"; }, 10); // 부드럽게 나타남

    // 3초 후 자동으로 사라짐
    alertTimeout = setTimeout(hideCustomAlert, 10000);
}

function hideCustomAlert() {
    var alertBox = document.getElementById("customAlert");
    clearTimeout(alertTimeout); // 기존 타이머 취소 (클릭 시 즉시 사라지게)
    alertBox.style.opacity = "0";

    setTimeout(() => { 
        alertBox.style.display = "none"; 
    }, 500); // transition과 동일한 시간
}
