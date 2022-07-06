import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NavbarComponent } from './components/navbar/navbar.component';
import { TmDashboardComponent } from './components/tm-dashboard/tm-dashboard.component';
import { StudentDashboardComponent } from './components/student-dashboard/student-dashboard.component';
import { ResultsComponent } from './components/results/results.component';
import { GradesComponent } from './components/grades/grades.component';
import { PractiseTestComponent } from './components/practise-test/practise-test.component';
import { TakeTestComponent } from './components/take-test/take-test.component';
import { CreateTestComponent } from './components/create-test/create-test.component';
import { PerformanceListComponent } from './components/performance-list/performance-list.component';
import { LandingPageComponent } from './components/landing-page/landing-page.component';
import { LoginComponent } from './components/login/login.component';
import { SignupComponent } from './components/signup/signup.component';
import { FormsModule } from '@angular/forms';
import { TmLandingComponent } from './components/tm-landing/tm-landing.component' ;

@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    TmDashboardComponent,
    StudentDashboardComponent,
    ResultsComponent,
    GradesComponent,
    PractiseTestComponent,
    TakeTestComponent,
    CreateTestComponent,
    PerformanceListComponent,
    LandingPageComponent,
    LoginComponent,
    SignupComponent,
    TmLandingComponent,
   
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule
  ],

  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
