/// <reference types="Cypress" />
class InTheCart {
    DELETE_BUTTONS = ".cart_quantity_delete";
    CHECKOUT_BUTTON = '.btn.btn-default.check_out';
  
    deleteItems(num_of_items: number): void {
        cy.get(this.DELETE_BUTTONS).then(deletes => {
            // randomly select items and delete them
            cy.wrap(deletes).its('length').then(length => {
                const itemsToDelete = Cypress._.take(deletes, Math.min(num_of_items, length));
                cy.wrap(itemsToDelete).each(item => cy.wrap(item).click());
            });
        });
    }

    proceedToCheckout(): void {
        // click the checkout button
        cy.get(this.CHECKOUT_BUTTON).click();
    }
}
export default InTheCart;
