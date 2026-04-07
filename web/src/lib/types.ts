export type InventoryType = {
  key: "ExtractedPlasmid" | "BacterialStock" | "SolidMediaPlate";
  label: string;
};

export type CollectionNode = {
  uri: string;
  display_id: string;
  name: string;
  description?: string;
  has_subcollections: boolean;
  storage_kind?: string;
};

export type AuthResponse = {
  authenticated: boolean;
  username: string | null;
};

export type CreateInventoryPayload = {
  destination_collection_uri: string;
  implementation_type: string;
  name?: string;
  notes?: string;
  built_uri?: string;
  barcode?: string;
  lot_id?: string;
  images: File[];
};

export type CreateInventoryResponse = {
  created_uri: string;
  destination_collection_uri: string;
  implementation_type: string;
  attached_images: number;
  message: string;
};
