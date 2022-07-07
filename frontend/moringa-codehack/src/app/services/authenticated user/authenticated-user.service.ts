import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { User } from 'src/app/classes/user/user';

@Injectable({
  providedIn: 'root',
})
export class AuthenticatedUserService {
  private url: string = 'http://localhost:8000/api/authenticated_user/';
  constructor(private httpClient: HttpClient) {}

  public getUser(): Observable<User[]> {
    return this.httpClient.get<User[]>(this.url);
  }
}
