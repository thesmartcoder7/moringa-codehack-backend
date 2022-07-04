import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import{ StudentDashboardComponent } from './components/student-dashboard/student-dashboard.component';
import { LandingPageComponent } from './components/landing-page/landing-page.component';
import { AssessmentComponent  } from './components/assessment/assessment.component';
import { PractiseTestComponent } from './components/practise-test/practise-test.component';
// import { HttpClientModule } from '@angular/common/http';

const routes: Routes = [
  { path: '', component: LandingPageComponent},
  { path: 'student-dashboard', component: StudentDashboardComponent},
  { path: 'assessment', component: AssessmentComponent},
  { path: 'practise-test', component: PractiseTestComponent},


];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
