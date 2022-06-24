import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { FormControl } from '@angular/forms';
import { AuthService } from 'src/app/services/auth.service';
import { GlobalService } from 'src/app/services/global.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {
  last_name = new FormControl('');
  first_name = new FormControl('');
  patronym = new FormControl('');
  group_number = new FormControl('');
  username = new FormControl('');
  password = new FormControl('');

  constructor(
    private authService: AuthService,
    private globalService: GlobalService,
    private router: Router
  ) { }

  ngOnInit(): void {
  }

  register() {
    const body = {
      last_name: this.last_name.value,
      first_name: this.first_name.value,
      patronym: this.patronym.value,
      group_number: this.group_number.value,
      username: this.username.value,
      password: this.password.value
    };

    this.authService.register(body).subscribe((res) => {
      this.globalService.setToken(res['token']);
      this.router.navigate(['/tests']);
    });
  }
}
