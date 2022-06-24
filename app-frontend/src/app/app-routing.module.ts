import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { AuthComponent } from './web/auth/auth.component';
import { AuthGuardService } from './guards/auth-guard.service';
import { UnAuthGuardService } from './guards/unauth-guard.service';
import { LoginComponent } from './web/auth/login/login.component';
import { RegisterComponent } from './web/auth/register/register.component';

import { TestsComponent } from './web/tests/tests.component';
import { TestResultComponent } from './web/tests/test-result/test-result.component';
import { TestDetailComponent } from './web/tests/test-detail/test-detail.component';
import { TestListComponent } from './web/tests/test-list/test-list.component';

const routes: Routes = [
  {
    path: 'auth',
    component: AuthComponent,
    canActivate: [UnAuthGuardService],
    children: [
      {
        path: '',
        redirectTo: 'login',
        pathMatch: 'full'
      },
      {
        path: 'login',
        component: LoginComponent
      },
      {
        path: 'register',
        component: RegisterComponent
      }
    ]
  },
  {
    path: 'tests',
    component: TestsComponent,
    canActivate: [AuthGuardService],
    children: [
      {
        path: '',
        redirectTo: 'all',
        pathMatch: 'full'
      },
      {
        path: 'all',
        component: TestListComponent
      },
      {
        path: ':slug',
        component: TestDetailComponent
      },
      {
        path: ':slug/result',
        component: TestResultComponent
      }
    ]
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
