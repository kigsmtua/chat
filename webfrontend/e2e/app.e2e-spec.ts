import { WebfrontendPage } from './app.po';

describe('webfrontend App', () => {
  let page: WebfrontendPage;

  beforeEach(() => {
    page = new WebfrontendPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
