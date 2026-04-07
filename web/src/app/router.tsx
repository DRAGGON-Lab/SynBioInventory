import { createBrowserRouter } from 'react-router-dom'

import { CollectionBrowserPage } from '../pages/CollectionBrowserPage'
import { CreateImplementationPage } from '../pages/CreateImplementationPage'
import { LoginPage } from '../pages/LoginPage'
import { ReviewSubmitPage } from '../pages/ReviewSubmitPage'
import { SuccessPage } from '../pages/SuccessPage'

export const router = createBrowserRouter([
  { path: '/', element: <LoginPage /> },
  { path: '/collections', element: <CollectionBrowserPage /> },
  { path: '/create', element: <CreateImplementationPage /> },
  { path: '/review', element: <ReviewSubmitPage /> },
  { path: '/success', element: <SuccessPage /> },
])
