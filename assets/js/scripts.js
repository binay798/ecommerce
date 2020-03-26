let items = document.querySelectorAll(".items");
for(let i=0;i<items.length;i++){
    items[i].addEventListener("mouseover",(item)=>{
        items[i].style.transform = "translateY(-20px)";
        items[i].style.transition = ".3s";
        items[i].style.cursor = "pointer";
    })
    items[i].addEventListener("mouseout",(item)=>{
        items[i].style.transform = "translateY(0px)";
    })
}

