import { Component, OnInit } from '@angular/core';

interface Assessment{
  title: string;
  language: string;
  dueDate: Date;
  timeLimit: number;
}

@Component({
  selector: 'app-assessment',
  templateUrl: './assessment.component.html',
  styleUrls: ['./assessment.component.css']
})

export class AssessmentComponent implements OnInit {
  public assessments: Assessment[]= [{
    title:'',
    language:'',
    dueDate:new Date(),
    timeLimit:30,

  }];

  constructor() { }

  ngOnInit(): void {
  }

}
