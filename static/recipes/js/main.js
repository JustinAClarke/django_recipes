document.getElementById("categories").onclick = function(){
    obj= document.getElementById("categoriesList");
    if(obj.style.display != "inline-block")
        obj.style.display = "inline-block";
    else
        obj.style.display = "none";
}

