var updateBtns = document.getElementsByClassName('update-cart')
if(updateBtns.length >0 ){    
    for (var i = 0; i < updateBtns.length; i++) {
        updateBtns[i].addEventListener('click', function () {
            var productId = this.dataset.producto
            var action = this.dataset.action
            var size = getSize(this)
            var color = getColor(this)            
            console.log(productId);
            console.log(action);
            console.log(size);
            console.log(color);
            console.log('USER:', user);
            if (user == 'AnonymousUser') {
                addCookieItem(productId, action)
            } else {
                updateUserOrder(productId, action)
            }
        })
    }    
}

function getSize(e) {
    console.log(e.parentElement);
    var size = e.parentElement.querySelector('.producto-tallas .talla.active')    
    return size.dataset.size
}
function getColor(e) {
    console.log(e);
}

function addCookieItem(productId, action) {
    console.log('Not logged in')
    // if (action == 'add') {
    //     if (cart[productId] == undefined) {
    //        cart[productId] = {'quantity': 1}
    //     } else {
    //         cart[productId]['quantity'] += 1
    //     }
    // }
    // if (action == 'remove') {
    //     cart[productId]['quantity'] -= 1
    //     if (cart[productId]['quantity'] <= 0) {
    //         console.log('Remove Item');
    //         delete cart[productId]
    //     }
    // }

    // console.log('Cart:',cart);
    // document.cookie = 'cart='+ JSON.stringify(cart) + ";domain=;path=/"
}

function updateUserOrder(productId, action) {

    var url = '/update_item/'
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            'productId': productId,
            'action': action
        })
    })
    .then((respose) => {
        return respose.json()
    })
    .then((data) => {
        console.log(data)        
    })

}