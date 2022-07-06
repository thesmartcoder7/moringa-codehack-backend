import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-landing-page',
  templateUrl: './landing-page.component.html',
  styleUrls: ['./landing-page.component.css'],
})
export class LandingPageComponent implements OnInit {
  message = 'Please login or signup';
  constructor(private http: HttpClient, private router: Router) {}

  ngOnInit(): void {
    //   this.http.get('http://localhost/8000/api/authenticated_user/').subscribe({
    //     next: (v) => console.log(v),
    //     error: (e) => console.error(e),
    //     complete: () => console.info('complete')
    // })
    this.http
      .get('http://localhost/8000/api/authenticated_user/', {
        withCredentials: true,
      })
      .subscribe({
        next: (res: any) => {
          console.log(res);
        },
        error: (error: any) => {
          console.log(error);
        },
        complete: () => {
          console.log('complete');
        },
      });
  }
}
