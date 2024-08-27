document.addEventListener("DOMContentLoaded", function () {
    const clockDiv = document.createElement("div");
    clockDiv.id = "clock";
    document.body.appendChild(clockDiv);

    // 初始化时钟
    updateClock();
    // 每秒更新一次时间
    setInterval(updateClock, 1000);
});

function updateClock() {
    const now = new Date();
    const year = now.getFullYear();
    const month = String(now.getMonth() + 1).padStart(2, "0"); // 月份从0开始
    const day = String(now.getDate()).padStart(2, "0");
    const hours = String(now.getHours()).padStart(2, "0");
    const minutes = String(now.getMinutes()).padStart(2, "0");
    const seconds = String(now.getSeconds()).padStart(2, "0");

    document.getElementById("clock").textContent =
        `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
}

