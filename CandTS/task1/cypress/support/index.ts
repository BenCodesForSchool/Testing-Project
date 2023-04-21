import 'cypress-xpath';

declare global {
  namespace Cypress {
    interface Chainable<Subject> {
      xpath(selector: string): Chainable<Element>;

      /**
       * Custom command to run Cucumber tests.
       */
      cucumber(): Chainable<any>;
    }
  }
}

Cypress.Commands.add('xpath', (selector: string): Cypress.Chainable<Element> => {
  return cy.xpath(selector);
});
