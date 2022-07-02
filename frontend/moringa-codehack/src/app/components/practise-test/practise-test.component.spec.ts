import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PractiseTestComponent } from './practise-test.component';

describe('PractiseTestComponent', () => {
  let component: PractiseTestComponent;
  let fixture: ComponentFixture<PractiseTestComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PractiseTestComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PractiseTestComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
