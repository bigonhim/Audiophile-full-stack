const cart = document.querySelector('.cart-box');
const close = document.getElementById('close');
const loader = document.querySelector(".loader");
const productsBackground = document.querySelector('.productsBackground');
const productBlurView = document.querySelector('.productBlurView');
const cartCircle = document.querySelector('.cartCircle');
const addButtons = document.querySelectorAll('.addCartButton');
const removeButtons = document.querySelectorAll('.removeCartButton');
const addToCartButtons = document.querySelectorAll('.addToCart');
const confirmDetails = document.querySelector('.confirmDetails');

addButtons.forEach(function(addButton) {
    addButton.addEventListener('click', function() {
        const targetId = this.getAttribute('data-target');
        const current = document.getElementById(targetId);
        let currentQuantity = parseInt(current.textContent);
        currentQuantity += 1;
        current.textContent = currentQuantity;

        const productId1 = this.getAttribute('data-product-id');
        const productId = parseInt(productId1);    
        const data = {
            quantity: currentQuantity,
            product_id : productId
        };
        console.log("Preparing to send data please be onstandby");
        const url = '/cartquantity/';
        fetch(url,{ 
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});

removeButtons.forEach(function(removeButton){
   removeButton.addEventListener('click', function(){
    const targetId = this.getAttribute('data-target');
    const current = document.getElementById(targetId);    
    let currentQuantity = parseInt(current.textContent);
    if(currentQuantity > 0){
    currentQuantity -= 1;
    current.textContent = currentQuantity;
        }
    const productId1 = this.getAttribute('data-product-id');
    const productId = parseInt(productId1);  

    const data = {
        quantity: currentQuantity,
        product_id : productId
    };
    const url = '/cartquantity/';
    fetch(url,{ 
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}); 
}); 

addToCartButtons.forEach(function(addToCartButton){
    addToCartButton.addEventListener('click', function(){
        console.log("Preparing to send data, please be on standby");
        let currentCartQuantity = parseInt(cartCircle.textContent);
        currentCartQuantity  += 1;
        cartCircle.textContent = currentCartQuantity;
        const productId1 = this.getAttribute('data-product-id');
        const productId2 = parseInt(productId1); 
        const productPrice1 = this.getAttribute('data-product-price');
        const productPrice = parseFloat(productPrice1);
        const productName = this.getAttribute('data-product-name');
        const productImage= this.getAttribute('data-product-image');
        const data = {
            product_id: productId2,
            product_price: productPrice,
            product_name: productName,
            product_image : productImage
        };
        console.log("Sending data...");
        const url = '/post/';
        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken') 
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())  // Parse the JSON response
        .then(data => {
            console.log('Success:', data);  
            const quantityElement = document.getElementById(`quantity-${data.product.pk}`);
            if (quantityElement) {
                quantityElement.textContent = data.quantity;
            } else {
                const cartItemHtml = `
                    <div class="order-summary" >
                        <img src="${data.product_image}" alt="${data.product_name}">
                        <div class="separate">
                            <h6>${data.product_name}</h6>
                            <p style="font-size: .6em;">$${data.product_price}</p>
                        </div>
                        <div class="cart-sum">
                            <img src="${addImage}" class="addCartButton" data-target="quantity-{{ forloop.counter }}"  data-product-id="{{ orderItem.product_pk }}">
                            <p class="current" id="quantity-${data.product.pk}">${data.quantity}</p>
                            <img src="${removeImage}" class="removeCartButton" data-target="quantity-{{ forloop.counter }}"   data-product-id="{{ orderItem.product_pk }}" >
                        </div>
                    </div>
                `;
                document.querySelector('.order-summary').insertAdjacentHTML('beforeBegin', cartItemHtml);
            }
        })
        .catch(error => {
            console.error('Error:', error);  // Log any errors that occur
        });
    });
})


try{
    confirmDetails.addEventListener('click',function(){
        const data = {
            name : document.getElementById('name').value,
            emailAddress : document.getElementById('emailAddress').value,
            phoneNumber : document.getElementById('phoneNumber').value,
            address : document.getElementById('address').value,
            zipcode : document.getElementById('zipcode').value,
            city : document.getElementById('city').value,
            country : document.getElementById('country').value
        }
        console.log("Preparing to send contact information");
        const url = '/checkoutinfo/';
        fetch(url,{
            method : 'POST',
            headers : {
                'Content-Type' : 'application/json',
                'X-CSRFToken' : getCookie('csrftoken')
            },
            body :  JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => {
            console.log("Success : " , data);
            alert("Checkout-Info Sent Successfully");
        })
        .catch(error => {
            console.error('Error : ', error);
        })
    
    });

} catch(error){
    console.error("An error occurred : ", error);
}



// Function to get the CSRF token from cookies (if needed)
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


function showSidebar(){
    const Sidebar = document.querySelector('.sidebar')
    Sidebar.style.display = 'flex';
}
function closeSidebar(){
    const Sidebar = document.querySelector('.sidebar')
    Sidebar.style.display = 'none';
} 
document.addEventListener('DOMContentLoaded', function(){
    cartIcon.addEventListener('click',function (){
        cart.style.display = 'Grid';
        productsBackground.style.filter ='blur(5px) grayscale(100%)';
    }); 
    cartIcon.addEventListener('click',function (){
        cart.style.display = 'Grid';
        productBlurView.style.filter = 'blur(5px) grayscale(100%)';
    }); 
    close.addEventListener('click',function close(){
        cart.style.display ='none';
        productsBackground.style.filter = 'none';
    });
    close.addEventListener('click',function close(){
        cart.style.display ='none';
        productBlurView.style.filter = 'none';
    });
})

window.addEventListener('load',()  =>{
    loader.classList.add("loader-hidden");
    loader.addEventListener("transitionend", () =>{
       document.body.removeChild('loader')
    })
})

function injectSpeedInsights() {
        console.log('Injecting Vercel Speed Insights...');
        const script = document.createElement('script');
        script.src = 'https://cdn.jsdelivr.net/npm/@vercel/speed-insights';
        script.async = true;
        document.head.appendChild(script);
    }
    // Call the function to inject Speed Insights when the page loads
    window.onload = injectSpeedInsights();



