"""
Image Processor - Simple & Clean
"""

from PIL import Image, ImageFilter, ImageEnhance
import requests

class ImageProcessor:
    
    def resize(self, image_path, scale, output_path):
        """Resize image (scale: 1-10, 10 = full size, 1 = very small)"""
        img = self._load_image(image_path)
        factor = scale / 10
        new_width = int(img.width * factor)
        new_height = int(img.height * factor)
        img.resize((new_width, new_height), Image.LANCZOS).save(output_path)
        print(f"Saved to {output_path} (scale: {scale}/10)")
    
    def apply_blur(self, image_path, intensity, output_path):
        """Apply blur (intensity: 1-10, 10 = very blurry)"""
        img = self._load_image(image_path)
        for _ in range(intensity):
            img = img.filter(ImageFilter.BLUR)
        img.save(output_path)
        print(f"Saved to {output_path} (blur: {intensity}/10)")
    
    def apply_sharpen(self, image_path, intensity, output_path):
        """Apply sharpen (intensity: 1-10, 10 = very sharp)"""
        img = self._load_image(image_path)
        for _ in range(intensity):
            img = img.filter(ImageFilter.SHARPEN)
        img.save(output_path)
        print(f"Saved to {output_path} (sharpen: {intensity}/10)")
    
    def brightness(self, image_path, level, output_path):
        """Adjust brightness (level: 1-10, 5 = normal, 10 = very bright, 1 = dark)"""
        img = self._load_image(image_path)
        factor = level / 5  # 5 is normal (1.0)
        ImageEnhance.Brightness(img).enhance(factor).save(output_path)
        print(f"Saved to {output_path} (brightness: {level}/10)")
    
    def contrast(self, image_path, level, output_path):
        """Adjust contrast (level: 1-10, 5 = normal, 10 = high contrast)"""
        img = self._load_image(image_path)
        factor = level / 5
        ImageEnhance.Contrast(img).enhance(factor).save(output_path)
        print(f"Saved to {output_path} (contrast: {level}/10)")
    
    def _load_image(self, image_path):
        """Load image from URL or local path"""
        if image_path.startswith('http'):
            response = requests.get(image_path)
            temp_file = "temp_image.jpg"
            with open(temp_file, 'wb') as f:
                f.write(response.content)
            return Image.open(temp_file)
        return Image.open(image_path)


# Example usage
if __name__ == "__main__":
    processor = ImageProcessor()
    
    # Example with cat image
    img = "https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?w=500"
    
    print("Image Processor - Enter values 1-10\n")
    
    # Get user input
    try:
        resize_val = int(input("Resize scale (1-10): "))
        blur_val = int(input("Blur intensity (1-10): "))
        sharp_val = int(input("Sharpen intensity (1-10): "))
        bright_val = int(input("Brightness level (1-10): "))
        contrast_val = int(input("Contrast level (1-10): "))
        
        print("\nProcessing...")
        processor.resize(img, resize_val, output_path="resized.jpg")
        processor.apply_blur(img, blur_val, output_path="blurred.jpg")
        processor.apply_sharpen(img, sharp_val, output_path="sharpened.jpg")
        processor.brightness(img, bright_val, output_path="bright.jpg")
        processor.contrast(img, contrast_val, output_path="contrast.jpg")
        
        print("\n✓ Done! Check the output files.")
    except ValueError:
        print("Error: Please enter numbers between 1-10")
