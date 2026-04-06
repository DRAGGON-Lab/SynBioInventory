import { ChangeEvent } from "react";

interface Props {
  images: File[];
  onChange: (images: File[]) => void;
}

export function ImageUploader({ images, onChange }: Props) {
  function onFilePick(event: ChangeEvent<HTMLInputElement>) {
    const picked = Array.from(event.target.files ?? []);
    onChange([...images, ...picked]);
  }

  function remove(index: number) {
    onChange(images.filter((_, i) => i !== index));
  }

  return (
    <section>
      <label>
        Evidence Images
        <input type="file" accept="image/*" multiple onChange={onFilePick} />
      </label>
      <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fill,minmax(90px,1fr))", gap: 8, marginTop: 8 }}>
        {images.map((image, index) => (
          <figure key={`${image.name}-${index}`} style={{ margin: 0 }}>
            <img
              src={URL.createObjectURL(image)}
              alt={image.name}
              style={{ width: "100%", height: 80, objectFit: "cover", borderRadius: 8 }}
            />
            <figcaption style={{ fontSize: 11 }}>{image.name}</figcaption>
            <button onClick={() => remove(index)}>Remove</button>
          </figure>
        ))}
      </div>
    </section>
  );
}
