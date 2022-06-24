import { Component, OnInit } from '@angular/core';
import { TestsService } from 'src/app/services/tests.service';

@Component({
  selector: 'app-test-list',
  templateUrl: './test-list.component.html',
  styleUrls: ['./test-list.component.css']
})
export class TestListComponent implements OnInit {

  tests;
  constructor(
    private testsService: TestsService
  ) { }

  ngOnInit(): void {
    this.testsService.getTests().subscribe((res) => {
      this.tests = res;
    });
  }

}
