import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TmLandingComponent } from './tm-landing.component';

describe('TmLandingComponent', () => {
  let component: TmLandingComponent;
  let fixture: ComponentFixture<TmLandingComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TmLandingComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(TmLandingComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
