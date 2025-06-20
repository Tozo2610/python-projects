theme=0
function switch_theme(){
    if (theme===0){
        document.getElementById("css").href="static/theme_light.css";
        document.getElementById("theme_button").src="static/lm.png"
        theme=1;
    }
    else{
        document.getElementById("css").href="static/theme_dark.css";
        document.getElementById("theme_button").src="static/dm.png"
        theme=0;
    }
}