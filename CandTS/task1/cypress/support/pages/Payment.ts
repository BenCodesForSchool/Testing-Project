export default class Payment {
    // Finding the text boxes for all relevant credit card information, as well as the button that submits credit card information and confirms the user's payment.
    private readonly NAME_ON_CARD = "input[name='name_on_card']";
    private readonly CARD_NUMBER = "input[name='card_number']";
    private readonly CVC = "input[name='cvc']";
    private readonly EXPIRATION_MONTH = "input[name='expiry_month']";
    private readonly EXPIRATION_YEAR = "input[name='expiry_year']";
    private readonly CONFIRM_PAYMENT_BUTTON = "button[id='submit']";

    // Sending specified credit card information to the corresponding text boxes
    inputPaymentInfo(nameOnCard: string, cardNumber: string, cVc: string, exMonth: string, exYear: string) {
        cy.get(this.NAME_ON_CARD).type(nameOnCard);
        cy.get(this.CARD_NUMBER).type(cardNumber);
        cy.get(this.CVC).type(cVc);
        cy.get(this.EXPIRATION_MONTH).type(exMonth);
        cy.get(this.EXPIRATION_YEAR).type(exYear);
    }
  
    // Clicking the confirm payment button
    confirmPayment() {
        cy.get(this.CONFIRM_PAYMENT_BUTTON).click();
    }
}

    