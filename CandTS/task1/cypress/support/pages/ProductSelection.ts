
/// <reference types="Cypress" />
export default class ProductSelection {
  //Finding the buy button for all shirts (or any specified product, really) on the page
  SHIRTS = ".productinfo.text-center a:contains('Add to cart')"
  //Finding the button that allows a user to continue shopping after having added an item to the cart
  CONTINUE_SHOPPING_BUTTON = "div.modal-footer button"
  //Finding the button that allows a user to view the cart after having added an item to the cart. Keeping a specific css selector for this because there is 
  //Another view cart button that can be selected with just a[href='/view_cart']
  VIEWCART = ".shop-menu.pull-right a[href='/view_cart']"
  //This is an ad that I gave up on trying to get rid of. If you stop using the adblocker, this thing will make your program not work like 4/6 of the time.
  BOTTOM_AD = ".grippy-host .down"

  addProductsToCart(numProducts: number): void {
    //clicking away the ad that appears at the bottom so that it doesn't interfere with clicking any of the selected shirts
    cy.get(this.BOTTOM_AD).should('be.visible').click()

    //A variable that helps count how many items have been added to the cart
    let numShirts = 0

    //Collecting all buy buttons into a data structure
    cy.get(this.SHIRTS).then((shirts) => {
      //Randomly selecting the specified (2, in this case) number of buy buttons for shirts 
      const selectedShirts = Cypress._.sampleSize(shirts, numProducts)

      for (const shirt of selectedShirts) {
        //Clicking the buy buttons for all selected shirts
        cy.wrap(shirt).click()

        //Counting how many buy buttons have been clicked
        numShirts++

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

