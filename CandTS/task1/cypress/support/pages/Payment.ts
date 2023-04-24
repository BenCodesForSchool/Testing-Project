export default class Payment {
    // Finding the text boxes for all relevant credit card information, as well as the button that submits credit card information and confirms the user's payment.
    private readonly NAME_ON_CARD = "input[name='name_on_card']";
    private readonly CARD_NUMBER = "input[name='card_number']";
    private readonly CVC = "input[name='cvc']";
    private readonly EXPIRATION_MONTH = "input[name='expiry_month']";
    private readonly EXPIRATION_YEAR = "input[name='expiry_year']";
    private readonly CONFIRM_PAYMENT_BUTTON = "button[id='submit']";

    // Sending specified credit card information to the corresponding text boxes
    inputPaymentInfo(nameoncard: string, cardnumber: string, cvc: string, exmonth: string, exyear: string) {
        cy.get(this.NAME_ON_CARD).type(nameoncard);
        cy.get(this.CARD_NUMBER).type(cardnumber);
        cy.get(this.CVC).type(cvc);
        cy.get(this.EXPIRATION_MONTH).type(exmonth);
        cy.get(this.EXPIRATION_YEAR).type(exyear);
    }
  
    // Clicking the confirm payment button
    confirmPayment() {
        cy.get(this.CONFIRM_PAYMENT_BUTTON).click();
    }
}

    
