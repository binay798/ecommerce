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
        product_incart:0,
    }
    products.push(product);
})




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





let carts = document.querySelectorAll(".add-cart");
for(let i=0;i<carts.length;i++){
    carts[i].addEventListener("click",()=>{
        cartNumber(products[i]);
        
        
    })
}




let currentNum = 0;
function cartNumber(product){
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
    setItems(product);
    
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

function setItems(product){
    
    let productInCart = localStorage.getItem("ProductsInCart");
    productInCart  = JSON.parse(productInCart);
    if(productInCart !=null){
        if(productInCart[product.product_name]== undefined){
            productInCart = {
                ...productInCart,
                [product.product_name]:product,
            }
        }
        productInCart[product.product_name].product_incart += 1;
        
        
        
        
    }
    else{
        
        product.product_incart = 1;
        productInCart = {
            [product.product_name]:product,
        };
        
    }
    localStorage.setItem("ProductsInCart",JSON.stringify(productInCart));
    
}




function loopingProducts(){
    let product_items = document.querySelector(".items_in_cart"); 
    let items = localStorage.getItem("ProductsInCart");
    items = JSON.parse(items);
    Object.values(items).map(item=>{
        product_items.innerHTML +=`
        <div class="col-4">${item.product_name}</div>
        <div class="col-4">${item.product_price}</div>
        <div class="col-4">${item.product_incart}</div>
        `
    })
}


document.querySelector(".checkout").addEventListener("click",()=>{
    window.alert("Your items will be delivered soon!!");
})







loopingProducts();


