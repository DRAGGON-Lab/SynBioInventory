export type InventoryTypeKey = "ExtractedPlasmid" | "BacterialStock" | "SolidMediaPlate";

export interface AuthMeResponse {
  authenticated: boolean;
  username?: string;
}

export interface CollectionNode {
  uri: string;
  display_id: string;
  name: string;
  description?: string;
  has_subcollections: boolean;
  storage_kind: string;
}

export interface CollectionListResponse {
  items: CollectionNode[];
}

export interface InventoryTypeOption {
  key: InventoryTypeKey;
  label: string;
}

export interface CreateInventoryPayload {
  destination_collection_uri: string;
  implementation_type: InventoryTypeKey;
  name?: string;
  notes?: string;
  barcode?: string;
  lot_id?: string;
  built_uri?: string;
  images: File[];
}

export interface InventoryCreateResponse {
  created_uri: string;
  destination_collection_uri: string;
  implementation_type: InventoryTypeKey;
  attached_images: number;
  message: string;
}
