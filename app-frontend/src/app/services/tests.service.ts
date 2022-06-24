import { GlobalService } from 'src/app/services/global.service';
import { EndpointsService } from './endpoints.service';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class TestsService {

  constructor(
    private http: HttpClient,
    private endpoints: EndpointsService,
    private globalService: GlobalService
  ) { }

  getTests() {
    return this.http.get(this.endpoints.tests(), {headers: this.globalService.headers()});
  }

  getTest(slug: string) {
    return this.http.get(this.endpoints.test(slug), {headers: this.globalService.headers()});
  }

  saveAnswer(body) {
    return this.http.patch(this.endpoints.saveAnswer(), body, {headers: this.globalService.headers()});
  }

  submitTest(body, slug) {
    return this.http.post(this.endpoints.submitTest(slug), body, {headers: this.globalService.headers()});
  }

}
