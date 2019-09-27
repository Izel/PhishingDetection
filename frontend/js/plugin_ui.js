var background = chrome.extension.getBackgroundPage();
var colors = {
    "-1":"#008000",
    "0":"#FFA500",
    "1":"#DC143C"
};
var featureList = document.getElementById("features");

chrome.tabs.query({ currentWindow: true, active: true }, function(tabs){
    var result = background.results[tabs[0].id];
    var isPhish = background.isPhish[tabs[0].id];
    var legitimatePercent = background.legitimatePercents[tabs[0].id];

    for(var key in result){
        var newFeature = document.createElement("li");
        //console.log(key);
        newFeature.textContent = key;
        //newFeature.className = "rounded";
        newFeature.style.backgroundColor=colors[result[key]];
        featureList.appendChild(newFeature);
    }
    
    $("#site_score").text(parseInt(legitimatePercent)+"%");
    if(isPhish) {
        $("#res-circle").css("background", "#DC143C");
        $("#site_msg").text("Warning! Phishing website detected!.");
        $("#site_score").text(parseInt(legitimatePercent)-20+"%");
    }
});

