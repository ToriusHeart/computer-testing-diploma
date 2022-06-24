import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { TestsService } from 'src/app/services/tests.service';

@Component({
  selector: 'app-test-detail',
  templateUrl: './test-detail.component.html',
  styleUrls: ['./test-detail.component.css']
})
export class TestDetailComponent implements OnInit {

  slug;
  test: any;
  currentIndex: number = 0;
  selectedAnswer: number;
  answers:any[] = [];

  constructor(
    private route: ActivatedRoute,
    private testsService: TestsService,
    private router: Router
  ) { }

  ngOnInit(): void {
    this.slug = this.route.snapshot.params['slug'];
    this.testsService.getTest(this.slug).subscribe((res) => {
      this.test = res['test'];
      if(this.test.students_set.completed) {
        this.router.navigate(['/tests/' + this.slug + '/result']);
      }
      this.initializeAnswers();
    });
  }
  initializeAnswers(){
    const usersAnswers = this.test.students_set.studentanswer_set;
    for(let i=0; i<usersAnswers.length; i++) {
      this.answers.push(usersAnswers[i]['answer']);
    }
    console.log(this.answers);
  }
  saveAnswer() {
    const body = {
      "student": this.test.students_set.id,
      "question" : this.test.question_set[this.currentIndex].id,
      "answer" : this.selectedAnswer
    }

    this.testsService.saveAnswer(body).subscribe((res) => {
      console.log(res);
    });
  }
  
  submitTest() {
    const body = {
      "student" : this.test.students_set.id,
      "question" : this.test.question_set[this.currentIndex].id,
      "answer" : this.selectedAnswer
    }
    
    this.testsService.submitTest(body, this.slug).subscribe((res) => {
      this.router.navigate(['/quizzes/' + this.slug + '/result']);
    });
  }

  next() {
    if(this.currentIndex === this.test.question_set.length-1) {
      this.submitTest();
      return;
    }
    
    if(this.selectedAnswer != null) {
      this.saveAnswer();
    }
    
    if(this.currentIndex !== this.test.question_set.length-1) {
      this.currentIndex += 1;
      this.selectedAnswer = null;
    }
  }
  
  selectAnswer(id: number) {
    console.log(id);
    this.selectedAnswer = id;
    this.answers[this.currentIndex] = id;
  }

  previous() {
    if(this.selectedAnswer != null) {
      this.saveAnswer();
    }

    if(this.currentIndex != 0) {
      this.currentIndex -= 1;
      this.selectedAnswer = null;
    }
  }

}
