import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css'],
})
export class SignupComponent implements OnInit {
  constructor(
    private http: HttpClient,
    private router: Router
    ) {}

  ngOnInit(): void {}

  submit(userName: string, userEmail: string, userPassword: string): void {
    console.log(userName, userEmail, userPassword)
    this.http
      .post('http://localhost:8000/api/register/', {
        username: userName,
        email: userEmail,
        password: userPassword,
      })
      .subscribe(()=> this.router.navigate(['/login']));
  }
}
