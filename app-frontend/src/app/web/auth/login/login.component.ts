import { Component, OnInit } from '@angular/core';
import { AuthService } from 'src/app/services/auth.service';
import { FormControl } from '@angular/forms';
import { GlobalService } from 'src/app/services/global.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  username = new FormControl('');
  password = new FormControl('');
  constructor(
    private authService: AuthService,
    private globalService: GlobalService,
    private router: Router
  ) { }

  ngOnInit(): void {
  }

  login() {
    const body = {
      username: this.username.value,
      password: this.password.value
    };
    this.authService.login(body).subscribe((res) => {
      this.globalService.setToken(res['token']);
      this.router.navigate(['/tests']);
    });
  };

}
