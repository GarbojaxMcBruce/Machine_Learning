using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using LinearMachineLearning.DataHandling;
using System.IO;

namespace LinearMachineLearning.LearningAlgorithms
{
    public class LinearModel
    {
        #region Parameters
        public string Name { get; set; }
        public string FilePath { get; set; }
        public int InputSize { get; set; }
        public double[] Inputs { get; set; }
        public double Output { get; set; }
        public double[] Weights { get; set; }
        public double InSampleError { get; set; }
        #endregion

        #region Constructors
        public LinearModel()
        {
            InputSize = 1;
            Inputs = new double[InputSize];
            Weights = new double[InputSize];
            Output = 0;
            InSampleError = 0;
        }
        
        public LinearModel(int inputSize)
        {
            InputSize = inputSize;
            Inputs = new double[InputSize];
            Weights = new double[InputSize];
            Output = 0;
            InSampleError = 0;
        }

        public LinearModel(string filePath)
        {
            FilePath = filePath;
            string[] lines = System.IO.File.ReadAllLines(filePath);

            Name = lines[0];
            InputSize = Convert.ToInt32(lines[1]);
            Inputs = new double[InputSize];
            Weights = new double[InputSize];

            string[] stringWeights = lines[2].Split(',');
            for(int index = 0; index < stringWeights.Length; index++)
            {
                Weights[index] = Convert.ToDouble(stringWeights[index]);
            }

            InSampleError = 0;
            Output = 0;
        }
        #endregion

        #region Methods
        public void SetInputs(double[] input)
        {
            for(int i = 0; i < InputSize; i++)
            {
                Inputs[i] = input[i];
            }
        }
        public virtual void ComputeOutput(double[] input)
        {
            if(input.Length != InputSize)
            {
                return;
            }
            SetInputs(input);
            Output = 0;
            for(int i = 0; i < InputSize; i++)
            {
                Output += Inputs[i] * Weights[i];
            }
        }
        public double ComputeAndReturnOutput(double[] input)
        {
            double output = 0;
            if (input.Length != InputSize)
            {
                return 0;
            }
            SetInputs(input);
            for (int i = 0; i < InputSize; i++)
            {
                output += Inputs[i] * Weights[i];
            }
            return output;
        }
        public virtual void Train(DataPoint point)
        {

        }
        public virtual void Learn(DataSet set)
        {

        }
        public virtual void ComputeInSampleError(DataSet set)
        {
            InSampleError = 0;
            foreach(DataPoint point in set.Examples)
            {
                InSampleError += ComputeSinglePointError(point);
            }
        }
        public virtual double ComputeSinglePointError(DataPoint point)
        {
            ComputeOutput(point.Input);
            return Math.Abs(Output - point.Output);
        }
        public void Save()
        {
            string[] lines = new string[3];
            lines[0] = Name;
            lines[1] = InputSize.ToString();
            for(int i = 0; i < InputSize - 1; i++)
            {
                lines[2] += Weights[i].ToString() + ",";
            }
            lines[2] += Weights[InputSize - 1];

            using(StreamWriter file = new StreamWriter(FilePath, false))
            {
                foreach(string line in lines)
                {
                    file.WriteLine(line);
                }
            }
        }
        public void Save(string filepath)
        {
            string[] lines = new string[3];
            lines[0] = Name;
            lines[1] = InputSize.ToString();
            for (int i = 0; i < InputSize - 1; i++)
            {
                lines[2] += Weights[i].ToString() + ",";
            }
            lines[2] += Weights[InputSize - 1];

            using (StreamWriter file = new StreamWriter(filepath, false))
            {
                foreach (string line in lines)
                {
                    file.WriteLine(line);
                }
            }
        }
        public void RandomizeWeights()
        {
            Random random = new Random();
            for(int j = 0; j < Weights.Length; j++)
            {
                double sum = 0;
                for(int i = 0; i < 10; i++)
                {
                    sum += (random.NextDouble() - .5) * 2;
                }
                Weights[j] = sum / 10;
            }
        }
        public void SimpleRandomPositiveWeights()
        {
            Random random = new Random();
            for(int i = 0; i < Weights.Length; i++)
            {
                Weights[i] = random.NextDouble();
            }
        }
        #endregion
    }
}
