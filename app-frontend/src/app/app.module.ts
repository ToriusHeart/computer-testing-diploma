import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { ReactiveFormsModule } from '@angular/forms';

import { AuthService } from './services/auth.service';
import { CookieService } from 'ngx-cookie-service';
import { EndpointsService } from './services/endpoints.service';
import { GlobalService } from './services/global.service';
import { AuthGuardService } from './guards/auth-guard.service';
import { UnAuthGuardService } from './guards/unauth-guard.service';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { AuthComponent } from './web/auth/auth.component';
import { LoginComponent } from './web/auth/login/login.component';
import { RegisterComponent } from './web/auth/register/register.component';
import { TestsComponent } from './web/tests/tests.component';
import { TestResultComponent } from './web/tests/test-result/test-result.component';
import { TestListComponent } from './web/tests/test-list/test-list.component';
import { TestDetailComponent } from './web/tests/test-detail/test-detail.component';
import { QuestionComponent } from './web/tests/test-detail/question/question.component';
import { AnswerComponent } from './web/tests/test-detail/question/answer/answer.component';
import { RecorderComponent } from './web/tests/test-detail/question/recorder/recorder.component';

@NgModule({
  declarations: [
    AppComponent,
    AuthComponent,
    LoginComponent,
    RegisterComponent,
    TestsComponent,
    TestResultComponent,
    TestListComponent,
    TestDetailComponent,
    QuestionComponent,
    AnswerComponent,
    RecorderComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    ReactiveFormsModule,
  ],
  providers: [
    AuthService,
    CookieService,
    EndpointsService,
    GlobalService,
    AuthGuardService,
    UnAuthGuardService,
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
