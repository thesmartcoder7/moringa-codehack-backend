import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TmDashboardComponent } from './tm-dashboard.component';

describe('TmDashboardComponent', () => {
  let component: TmDashboardComponent;
  let fixture: ComponentFixture<TmDashboardComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TmDashboardComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(TmDashboardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
