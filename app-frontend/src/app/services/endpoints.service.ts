import { Injectable } from '@angular/core';
import { GlobalService } from './global.service';

@Injectable({
  providedIn: 'root'
})
export class EndpointsService {

  constructor(
      private globalService: GlobalService
  ) { }

  login() {
    return this.globalService.apiHost + 'auth/login/';
  }

  register() {
    return this.globalService.apiHost + 'auth/register/';
  }

  tests() {
    return this.globalService.apiHost + 'tests/';
  }

  test(slug: string) {
    return this.globalService.apiHost + 'tests/' + slug + "/";
  }

  saveAnswer() {
    return this.globalService.apiHost + 'save-answer/';
  }

  submitTest(slug: string) {
    return this.globalService.apiHost + 'tests/' + slug + "/submit/";
  }
}
