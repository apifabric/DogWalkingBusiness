import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { WalkerHomeComponent } from './home/Walker-home.component';
import { WalkerNewComponent } from './new/Walker-new.component';
import { WalkerDetailComponent } from './detail/Walker-detail.component';

const routes: Routes = [
  {path: '', component: WalkerHomeComponent},
  { path: 'new', component: WalkerNewComponent },
  { path: ':id', component: WalkerDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Walker-detail-permissions'
      }
    }
  },{
    path: ':walker_id/Booking', loadChildren: () => import('../Booking/Booking.module').then(m => m.BookingModule),
    data: {
        oPermission: {
            permissionId: 'Booking-detail-permissions'
        }
    }
},{
    path: ':walker_id/Feedback', loadChildren: () => import('../Feedback/Feedback.module').then(m => m.FeedbackModule),
    data: {
        oPermission: {
            permissionId: 'Feedback-detail-permissions'
        }
    }
},{
    path: ':walker_id/Schedule', loadChildren: () => import('../Schedule/Schedule.module').then(m => m.ScheduleModule),
    data: {
        oPermission: {
            permissionId: 'Schedule-detail-permissions'
        }
    }
},{
    path: ':walker_id/Walk', loadChildren: () => import('../Walk/Walk.module').then(m => m.WalkModule),
    data: {
        oPermission: {
            permissionId: 'Walk-detail-permissions'
        }
    }
},{
    path: ':walker_id/WalkerPayment', loadChildren: () => import('../WalkerPayment/WalkerPayment.module').then(m => m.WalkerPaymentModule),
    data: {
        oPermission: {
            permissionId: 'WalkerPayment-detail-permissions'
        }
    }
}
];

export const WALKER_MODULE_DECLARATIONS = [
    WalkerHomeComponent,
    WalkerNewComponent,
    WalkerDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class WalkerRoutingModule { }