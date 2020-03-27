let items = document.querySelectorAll(".items");

products = [];



items.forEach((item,index)=>{
    let name=item.querySelector(".name").textContent;
    let price = item.querySelector(".price").textContent;
    let image = item.querySelector(".image").src;
    let product = {
        product_name:name,
        product_price:price,
        product_image:image,
    }
    products.push(product);
})
console.log(products);



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

let carts = document.querySelectorAll("button");
for(let i=0;i<carts.length;i++){
    carts[i].addEventListener("click",()=>{
        cartNumber();
    })
}

let currentNum = 0;
function cartNumber(){
    let checkValueInCart = localStorage.getItem("cartNumber");
    checkValueInCart = parseInt(checkValueInCart);

    if(checkValueInCart){
        
        localStorage.setItem("cartNumber",checkValueInCart+1)
        document.querySelector(".cart_increase").textContent = checkValueInCart+1;
    }
    else{
        localStorage.setItem("cartNumber",1);
        document.querySelector(".cart_increase").textContent=1;
    }
    
    
}
function onLoadCartNumber(){
    let cartExists = localStorage.getItem("cartNumber");
    if(cartExists){
        document.querySelector(".cart_increase").textContent = cartExists;
    }
    else{
        document.querySelector(".cart_increase").textContent = 0;
    }
}















onLoadCartNumber();