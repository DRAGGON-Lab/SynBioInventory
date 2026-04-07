export type CollectionSummary = {
  uri: string
  display_id: string
  name: string
  description?: string | null
  has_subcollections: boolean
}

export type InventoryTypeSummary = {
  key: 'ExtractedPlasmid' | 'BacterialStock' | 'SolidMediaPlate'
  label: string
}

export type CreateInventoryRequest = {
  destinationCollectionUri: string
  destinationStorageKind: string
  implementationType: string
  objectUri: string
  barcode?: string
  lotId?: string
  notes?: string
  builtUri?: string
  images: File[]
}

export type CreateInventoryResponse = {
  created_uri: string
  destination_collection_uri: string
  implementation_type: string
  attached_images: number
  message: string
  rdf_xml_preview: string
}
