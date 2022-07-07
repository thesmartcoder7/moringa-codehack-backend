import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import {Observable,of, from } from 'rxjs';
import { map, catchError } from 'rxjs/operators';

@Component({
  selector: 'app-landing-page',
  templateUrl: './landing-page.component.html',
  styleUrls: ['./landing-page.component.css'],
})
export class LandingPageComponent implements OnInit {
  message = 'Please login or signup';

  constructor(private http: HttpClient, private router: Router) {}

  ngOnInit(): void {
      this.http.get('http://localhost/8000/api/authenticated_user/').subscribe({
        next: (v) => console.log(v),
        error: (e) => console.error(e),
        complete: () => console.info('complete')
    })
  }
}
