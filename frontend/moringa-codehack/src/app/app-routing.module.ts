import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LandingPageComponent } from './components/landing-page/landing-page.component';
import { LoginComponent } from './components/login/login.component';
import { SignupComponent } from './components/signup/signup.component';
import{ StudentDashboardComponent } from './components/student-dashboard/student-dashboard.component';
import { LandingPageComponent } from './components/landing-page/landing-page.component';
// import { HttpClientModule } from '@angular/common/http';

const routes: Routes = [
  {path:'',component:LandingPageComponent},
  {path:'login',component:LoginComponent},
  {path:'signup',component:SignupComponent},
  { path: '', component: LandingPageComponent},
  { path: 'student-dashboard', component: StudentDashboardComponent}
 
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
