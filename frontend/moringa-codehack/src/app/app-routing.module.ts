import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LandingPageComponent } from './components/landing-page/landing-page.component';
import { LoginComponent } from './components/login/login.component';
import { SignupComponent } from './components/signup/signup.component';
import { TmDashboardComponent } from './components/tm-dashboard/tm-dashboard.component';
import { TmLandingComponent  } from './components/tm-landing/tm-landing.component';

const routes: Routes = [
  {path: '', redirectTo:'landing', pathMatch:'full'},
  {path:'landing',component:LandingPageComponent},
  {path:'login',component:LoginComponent},
  {path:'signup',component:SignupComponent},
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

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
