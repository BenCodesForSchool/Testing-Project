/// <reference types="Cypress" />
export default class ProductSelection {
    //Finding the buy button for all shirts (or any specified product, really) on the page
    SHIRTS = ".productinfo.text-center a:contains('Add to cart')"
    //Finding the button that allows a user to continue shopping after having added an item to the cart
    CONTINUE_SHOPPING_BUTTON = "div.modal-footer button"
    //Finding the button that allows a user to view the cart after having added an item to the cart. Keeping a specific css selector for this because there is 
    //Another view cart button that can be selected with just a[href='/view_cart']
    VIEWCART = ".shop-menu.pull-right a[href='/view_cart']"


    addProductsToCart(numProducts: number): void {
        //Collecting all buy buttons into an array
        cy.get(this.SHIRTS).then((shirts) => {
            //Clicking numProducts amount of shirts
            for (let i = 0; i < numProducts; i++) {
                const randomIndex = Math.floor(Math.random() * shirts.length);
                const randomShirt = shirts[randomIndex];
                cy.wrap(randomShirt).click();
                //Clicking on the continue shopping button after each shirt is selected
                cy.get(this.CONTINUE_SHOPPING_BUTTON).click()
            }
        })
    }

    viewCart(): void {
        //Clicking the view cart button
        cy.get(this.VIEWCART).click()
    }
}

