import { CanActivateFn, Router } from '@angular/router';

export const routerGuardGuard: CanActivateFn = (route, state) => {

  new Router().navigateByUrl('access-denied')
  return false;
};
