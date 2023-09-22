    $(document).ready(function () {
    $('.add-to-cart-button').on('click', function () {
        const isAuthenticated = $(this).data('authenticated');
        if (isAuthenticated === true) {
            let product_id = $(this).data('product-id');
            let product_qty = $(this).closest('.products').find('.quantity-input').val();
            let token = $('input[name=csrfmiddlewaretoken]').val()
            $.ajax({
                method: 'POST',
                url: '/products/add_to_cart/' + product_id + '/',
                dataType: 'json',
                data: {
                    'product_id': product_id,
                    'product_qty': product_qty,
                    csrfmiddlewaretoken: token
                },
                success: function () {
                    const popup = document.getElementById('popup');
                    popup.style.display = 'block';
                    // After 2 seconds, hide the popup
                    setTimeout(function () {
                        popup.style.display = 'none';
                    }, 2000);
                },
                error: function () {
                    alert('Error adding product to cart.');
                }
            });
        }
        else {
            window.location.href = '/accounts/login/';
        }
    });
});

    $(document).ready(function () {
        $('.increment-btn').click(function (e) {
            e.preventDefault();

            let inc_value = $(this).closest('.add-to-cart').find('.quantity-input').val();
            let value = parseInt(inc_value, 10);
            value = isNaN(value) ? 0 : value;
            if(value < 10){
                value++;
                $(this).closest('.add-to-cart').find('.quantity-input').val(value);
            }
        })
    })

    $(document).ready(function () {
        $('.decrement-btn').click(function (e) {
            e.preventDefault();

            let dec_value = $(this).closest('.add-to-cart').find('.quantity-input').val();
            let value = parseInt(dec_value, 10);
            value = isNaN(value) ? 1 : value;
            if(value > 1){
                value-=1;
                $(this).closest('.add-to-cart').find('.quantity-input').val(value);
            }
        })
    })


window.addEventListener('DOMContentLoaded', event => {
    // Navbar shrink function
    var navbarShrink = function () {
        const cartClass = document.body.querySelector('.cart')
        const teamTag = document.body.querySelector('#team')
        const navbarCollapsible = document.body.querySelector('#mainNav');
        if (!navbarCollapsible) {
            return;
        }
        if (window.scrollY === 0 && !cartClass && !teamTag) {
            navbarCollapsible.classList.remove('navbar-shrink')
        } else {
            navbarCollapsible.classList.add('navbar-shrink')
        }

    };

    // Shrink the navbar
    navbarShrink();

    // Shrink the navbar when page is scrolled
    document.addEventListener('scroll', navbarShrink);

    //  Activate Bootstrap scrollspy on the main nav element
    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            rootMargin: '0px 0px -40%',
        });
    }

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });

});

inc_value = parseInt

const rate = (product_id, rating) => {
    const isAuthenticated = $('.star-class').data('authenticated');
    if (isAuthenticated === true) {
        fetch(`/products/rate/${product_id}/${rating}/`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(rest => {
            window.location.reload();
        })}
    else {
        window.location.href = '/accounts/login/';
    }
}