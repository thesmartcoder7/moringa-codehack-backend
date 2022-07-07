import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LandingPageComponent } from './components/landing-page/landing-page.component';
import { LoginComponent } from './components/login/login.component';
import { SignupComponent } from './components/signup/signup.component';
import { TmDashboardComponent } from './components/tm-dashboard/tm-dashboard.component';
import { TmLandingComponent  } from './components/tm-landing/tm-landing.component';
import{ StudentDashboardComponent } from './components/student-dashboard/student-dashboard.component';
import { AssessmentComponent  } from './components/assessment/assessment.component';
import { PractiseTestComponent } from './components/practise-test/practise-test.component';
import { TakeTestComponent} from './components/take-test/take-test.component';
import { CreateTestComponent } from './components/create-test/create-test.component';
import { PerformanceListComponent } from './components/performance-list/performance-list.component';
import { GradesComponent } from './components/grades/grades.component';
// import { HttpClientModule } from '@angular/common/http';

const routes: Routes = [
  {path:'',component:LandingPageComponent},
  {path:'landing',component:LandingPageComponent},
  {path:'login',component:LoginComponent},
  {path:'signup',component:SignupComponent},
  { path: 'student-dashboard', component: StudentDashboardComponent},
  { path: 'assessment', component: AssessmentComponent},
  { path: 'practise-test', component: PractiseTestComponent},
  { path: 'take-test', component: TakeTestComponent },
  {path:'tmlanding', component:TmLandingComponent},
  {path:'tmdashboard', component:TmDashboardComponent},
  {path:'tmlanding/login', component:TmLandingComponent,   
children:[{
  path:'', component:LoginComponent
}]},
{path:'tmlanding/dashboard', component:TmLandingComponent,
children:[{
  path:'', component:TmDashboardComponent
}]},
{path:'tmlanding/create-test', component:TmLandingComponent,
children:[{
  path:'', component:CreateTestComponent
}]},
{path:'tmlanding/peformance-list', component:TmLandingComponent,
children:[{
  path:'', component:PerformanceListComponent
}]},
{path:'tmlanding/grades', component:TmLandingComponent,
children:[{
  path:'', component:GradesComponent
}]},

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
