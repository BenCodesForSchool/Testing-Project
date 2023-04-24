import 'cypress-xpath';

declare global {
    interface Chainable<Subject> {

      /**
       * Custom command to run Cucumber tests.
       */
      cucumber(): Chainable<Subject>;
    }
}

